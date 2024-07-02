from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        valid_types = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}

        if influencer_type not in valid_types:
            return f"{influencer_type} is not an allowed influencer type."

        if self._find_influencer_by_username(username, self.influencers) is not None:
            return f"{username} is already registered."

        new_influencer = valid_types[influencer_type](username, followers, engagement_rate)

        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        valid_campaigns = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

        if campaign_type not in valid_campaigns:
            return f"{campaign_type} is not a valid campaign type."

        if self._find_campaign_by_id(campaign_id, self.campaigns) is not None:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = valid_campaigns[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        curr_influencer = self._find_influencer_by_username(influencer_username, self.influencers)
        curr_campaign = self._find_campaign_by_id(campaign_id, self.campaigns)

        if curr_influencer is None:
            return f"Influencer '{influencer_username}' not found."

        if curr_campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not curr_campaign.check_eligibility(curr_influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        if curr_influencer.calculate_payment(curr_campaign) > 0.0:
            curr_campaign.approved_influencers.append(curr_influencer)
            curr_campaign.budget -= curr_influencer.calculate_payment(curr_campaign)
            curr_influencer.campaigns_participated.append(curr_campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        my_dict = {}

        for camp in self.campaigns:
            if camp.approved_influencers:
                for influencer in camp.approved_influencers:
                    if camp not in my_dict:
                        my_dict[camp] = 0
                    my_dict[camp] += influencer.reached_followers(camp.TYPE_)

        return my_dict

    def influencer_campaign_report(self, username: str):
        curr_influencer = self._find_influencer_by_username(username, self.influencers)
        return curr_influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        output = ["$$ Campaign Statistics $$"]

        for camp in sorted_campaigns:
            total_reached_followers_by_campaign = 0
            for influencer in camp.approved_influencers:
                total_reached_followers_by_campaign += influencer.reached_followers(camp.TYPE_)

            curr_output = [f"  * Brand: {camp.brand}, Total influencers: {len(camp.approved_influencers)},"
                           f" Total budget: ${camp.budget:.2f},"
                           f" Total reached followers: {total_reached_followers_by_campaign}"]
            output.extend(curr_output)

        return '\n'.join(output)


    # HELPER METHODS
    @staticmethod
    def _find_influencer_by_username(username, collection):
        influencer = [influ for influ in collection if influ.username == username]
        return influencer[0] if influencer else None

    @staticmethod
    def _find_campaign_by_id(camp_id, collection):
        campaign = [camp for camp in collection if camp.campaign_id == camp_id]
        return campaign[0] if campaign else None
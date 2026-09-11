package net.hibiscus.naturespirit.datagen;

import net.minecraft.core.HolderLookup;
import net.minecraft.core.registries.Registries;
import net.minecraft.data.PackOutput;
import net.minecraft.data.tags.TagAppender;
import net.minecraft.data.tags.TagsProvider;
import net.minecraft.tags.VillagerTradeTags;
import net.minecraft.world.item.trading.VillagerTrade;

import java.util.concurrent.CompletableFuture;

public class NSVillagerTradeTagsProvider extends TagsProvider<VillagerTrade> {

  public NSVillagerTradeTagsProvider(PackOutput output, CompletableFuture<HolderLookup.Provider> lookupProvider) {
    super(output, Registries.VILLAGER_TRADE, lookupProvider);
  }

  @Override
  protected void addTags(HolderLookup.Provider registries) {
    TagAppender<VillagerTrade> common = tag(VillagerTradeTags.WANDERING_TRADER_COMMON);
    NSVillagerTrades.WANDERING_TRADER_COMMON.forEach(trade -> common.add(trade.key()));
  }
}

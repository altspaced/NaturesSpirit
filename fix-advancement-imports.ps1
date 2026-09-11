$root = 'C:\Users\altsp\Desktop\NaturesSpirit-26.2\common\src\main\java'
$repls = @{
  'import net.minecraft.advancements.CriteriaTriggers;' = 'import net.minecraft.advancements.triggers.CriteriaTriggers;'
  'import net.minecraft.advancements.Criterion;' = 'import net.minecraft.advancements.triggers.Criterion;'
  'import net.minecraft.advancements.CriterionTrigger;' = 'import net.minecraft.advancements.triggers.CriterionTrigger;'
  'import net.minecraft.advancements.criterion.ContextAwarePredicate;' = 'import net.minecraft.advancements.predicates.ContextAwarePredicate;'
  'import net.minecraft.advancements.criterion.EntityPredicate;' = 'import net.minecraft.advancements.predicates.entity.EntityPredicate;'
  'import net.minecraft.advancements.criterion.SimpleCriterionTrigger;' = 'import net.minecraft.advancements.triggers.SimpleCriterionTrigger;'
}
Get-ChildItem -Path $root -Filter *.java -Recurse | ForEach-Object {
  $c = [IO.File]::ReadAllText($_.FullName)
  $n = $c
  foreach ($k in $repls.Keys) { $n = $n.Replace($k, $repls[$k]) }
  if ($n -ne $c) {
    [IO.File]::WriteAllText($_.FullName, $n)
    Write-Output $_.FullName
  }
}

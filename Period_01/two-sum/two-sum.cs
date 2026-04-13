// https://leetcode.com/problems/two-sum/submissions/1977586233

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // Оптимизация 2 - выделить память сразу
        var dict = new Dictionary<int, int>(nums.Length);
    
        for (int i = 0; i < nums.Length; i++) {
            int complement = target - nums[i];
        
            // Оптимизация 1: Одно обращение к словарю вместо двух
            if (dict.TryGetValue(complement, out int index)) {
                return new int[] { index, i };
            }
        
            /* Оптимизация 3: Прямое присваивание без ContainsKey
            Если число уже встречалось, мы можем просто перезаписать его индекс 
            (новый индекс всегда больше, и для поиска пары это неважно, 
            так как ответ либо найдется сейчас, либо никогда).*/
            dict[nums[i]] = i;
        }
    
        return new int[0]; // или выбросить исключение, если решение не найдено
    }
}
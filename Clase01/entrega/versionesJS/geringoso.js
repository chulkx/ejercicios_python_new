

function translate (text) {
    
    
    sentence =  text;
    //console.log(sentence);

    if (sentence == '') {
        sentence = 'Geringoso'
    }
    
    newSentence = sentence.split(" ");
//    newWord = '';
    outputSentence = '';
//    context = ('','');
    //console.log(newSentence);
    vowels = 'aeiouAEIOUáéíóú'
    rules = [('u','a'), ('u','e'), ('u','i'),('u','o'), ('o','i'), ('o','u'),
    ('i','a'), ('i','e'), ('i','o'),('i','u'), ('e','i'), ('e','u'),
    ('a','e'),('a','i'), ('a','o'), ('a','u')];
    
    newSentence.forEach((word) => {
        
        newWord = '';
        //console.log(word);
        for (let i = 0; i < word.length; i++) {
            letter = word.charAt(i);
            //console.log(letter);
            if (i == word.length-1) {
                context = (word[i], '');
            } else {
                context = (word[i], word[i+1]);
            }
            //console.log(context);
            if (vowels.includes(letter) & !rules.includes(context)) {
                newWord += letter.replace(letter, (letter + 'p' + letter));
            } else {
                newWord += word[i];
            }
        };
        outputSentence += newWord + ' ';            
    });
    console.log(outputSentence);
           
};

translate('cadena a convertir en geringoso, quien sabe, quizas funciona, maestro');
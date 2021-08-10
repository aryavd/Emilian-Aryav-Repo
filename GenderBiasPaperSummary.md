<html>
    <p>By: Emilian Sega</p>
    <ul>
        <li>
            The major problem in the paper is noticing the inherent gender bias within ELMo, and how that can easily alter results. Some other issues are that ELMo is trained on unequal data, and that it unequally encodes information about male and female entities.
        </li>
        <li>
            The method used in the paper is the model ELMo, and using that with datasets. The pros of ELMo is that you can find the cons easily, and that you can actually eliminate bias with certain methods. However, one of the major cons is that ELMo is trained on unequal data. In the training data used, there are significantly more male than female entities, making the method pretty unreliable at face value. But, this could easily be mitigated with certain methods that change the database which ELMo is trained on, these being data augmentation, which is the more reliable and better working solution, and neutralization, which works with smaller datasets. 
        </li>
        <li>
            The method was evaluated through the use of multiple datasets, in a way which showed the inherent bias that lies within. Another way they tested the method was when they switched the pronouns within certain sentences. The result was a separation of male and female component groups, in which occupations that typically males do were perceived as males, and the same for females.
        </li>
        <li>
            I thought that the evaluation they did was pretty good. It spans across the full spectrum of revealing the bias within ELMo, all the way to testing it, and eventually lowering it, which is exactly what we wish to achieve in this project.
        </li>
        <li>
            It seems that the method could be used, but is not the best because of the bias that’s already integrated within the method, which we will later have to eliminate by using one of the two tricks. I think that we could use it, but it’ll be a hassle, and maybe there is something better out there. However, we can definitely reuse the methods of data augmentation and neutralization to help eliminate any bias in any other methods, since these are really helpful.
        </li>
        <li>
            We should keep in mind the concepts of data augmentation and neutralization to eliminate bias. These can not only be used in ELMo, but for other tests too, and could potentially even be paired with CheckList.
        </li>
    </ul>
</html>

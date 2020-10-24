# Calclate the digits of 𝜋
---

Here i scoured the internet to find the different ways to calculate the digits of 𝜋

1. **[Issac Newtons's Method](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Issac%20Newtons%20Method.py "Go to Script")** : Got inspiration from Matt Parker's "Calculate pi by    hand Video [Youtube video](https://www.youtube.com/watch?v=CKl1B8y4qXw "Matt Parker's video")
   <details>
   <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\pi=\frac{3\sqrt{3}}{4}+24\left(\frac{1}{12}-\frac{1}{5.2^5}-\frac{1}{7.2^9}-\frac{1}{9.2^{12}}-.....\right)">
  </details>  

2. **[Chudnovsky algorithm](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Chudnovsky%20Algorithm.py "Go to Script")** : This is also from Matt Parker's another video [Youtube video](https://www.youtube.com/watch?v=LhlqCJjbEa0 "Other Video")
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\dpi{400}\Large&space;\pi=\frac{426880\sqrt{10005}}{\sum_{k=0}^{\infty}\frac{(6k)!(545140134k+13591409)}{(3k)!(k!)^3(-262537412640768000^k)}}">
    </details>

3. **[Basel Problem](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Basel%20Problem.py "Go to Script")** : From the famous Euler's Equation(Basel problem) 
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\pi=\sum_{n=1}^{\infty}\frac{1}{n^2}">
    </details>

4. **[Archemedes method](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Archemedes%20method.py "Go to Script")** : Archemedes method is used 
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\lim_{n\to\infty}n\sin(\frac{180}{n})">
    </details>

5. **[Nilakantha Series](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Nilakantha%20Series.py "Go to Script")** : Nilakantha Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\pi=3+\frac{4}{2\times3\times4}+\frac{4}{4\times5\times6}+\frac{4}{6\times7\times8}.....">
    </details>

6. **[Ramanujan's Method](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Ramanujan's%20Method.py "Go to Script")** : Srinivasa Ramanujan's Method using Modular arithmetic
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{1}{\pi}=\frac{2\sqrt{2}}{9801}\sum_{k=0}^{\infty}\frac{(4k)!(1103+26390k)}{(k!)^4(396^{4k})}">
    </details>

7. **[Spigot Algorithm](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Spigot%20Algorithm.py "Go to Script")** : Spigot Algorithm
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\pi=\sum_{k=0}^{k=\infty}\frac{1}{16^k}\left(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\right)">
    </details>

8. **[Half-area of a circle](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Half-area%20of%20a%20circle.py "Go to Script")** : Definite Integrals : from half-area of a circle
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi}{2}=\int_{-1}^{1}\sqrt{1-x^2}dx">
    </details>

9. **[Euler's Convergence Improvement Transformation](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Euler%20Convergence.py "Go to Script")** 
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi}{2}=\sum_{n=0}^{\infty}\frac{n!}{(2n+1){!!}}"/>

      [Referance](https://mathworld.wolfram.com/PiFormulas.html "Click this")
    </details>

10. **[From Known Identity Of Inverse Trignometric Function](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/taninverse.py "Go to Script")**
    <details>
    <summary>Click to view Formula</summary>
       <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi}{4}=\tan^{-1}(1)=\int_{0}^{1}\frac{1}{1+x^2}dx"/>
    </details>

11. **[BBP formula( Bailey–Borwein–Plouffe formula)-I](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/BBP%20Formula%20-%20I.py "Go to Script")** : 
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\dpi{800}\Large&space;\pi=\int_{0}^{1}\frac{16y-16}{y^4-2y^3+4y-4}dy"/>
      [Referance](https://mathworld.wolfram.com/PiFormulas.html "Wolfram Mathworld")
    </details>

12. **[BBP formula( Bailey–Borwein–Plouffe formula)-II](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/BBP%20Formula%20-%20II.py "Go to Script")**: A rapidly converging BBP-type formula found by **F. Bellard**
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\dpi{800}\Large&space;\pi=\frac{1}{2^6}\sum_{n=0}^{\infty}\frac{(-1)^n}{2^{10n}}\left(-\frac{2^5}{4n+1}-\frac{1}{4n+3}+\frac{2^8}{10n+1}-\frac{2^6}{10n+3}-\frac{2^2}{10n+5}-\frac{2^2}{10n+7}+\frac{1}{10n+9}\right)"/>
      [Referance](https://mathworld.wolfram.com/PiFormulas.html "Wolfram Mathworld")
    </details>

13. **[Viète's formula](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Viete%20Formuls.py "Go to Script")** : infinite product of nested radicals named after **François Viète**
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\dpi{800}\Large&space;\frac{2}{\pi}=\frac{\sqrt{2}}{2}.\frac{\sqrt{2+\sqrt{2}}}{2}.\frac{\sqrt{2+\sqrt{2+\sqrt{2}}}}{2}..."/>
    </details>

14. **[Basel Problem and Reiman Zeta Function](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Basel%20Problem%20-%20II.py "Go tot Script")** : This appears when integrating Planck's law to derive the Stefan–Boltzmann law in physics.[Referance](https://en.wikipedia.org/wiki/Riemann_zeta_function "Riemann zeta function")
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\dpi{800}\Large&space;\frac{\pi^4}{90}=\frac{1}{1^4}+\frac{1}{2^4}+\frac{1}{3^4}+\frac{1}{4^4}+...."/>
    </details>

15. **[Gregory-Leibniz Series - I](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Gregory-Leibiniz%20Series-I.py "Go tot Script")** :  Gregory-Leibniz Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi}{4}=1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\frac{1}{9}.....">
    </details>

16. **[Gregory-Leibniz Series - II](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Gregory-Leibiniz%20Series-II.py "Go tot Script")** :  Gregory-Leibniz Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi^2}{12}=\frac{1}{1^2}-\frac{1}{2^2}+\frac{1}{3^2}-\frac{1}{4^2}+\frac{1}{5^2}.....">
    </details>

17. **[Gregory-Leibniz Series - III](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Gregory-Leibiniz%20Series-III.py "Go tot Script")** :  Gregory-Leibniz Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi^2}{24}=\frac{1}{2^2}+\frac{1}{4^2}+\frac{1}{6^2}+\frac{1}{8^2}+\frac{1}{10^2}.....">
    </details>

18. **[Gregory-Leibniz Series - IV](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Gregory-Leibiniz%20Series-IV.py "Go tot Script")** :  Gregory-Leibniz Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi^2}{8}=\frac{1}{1^2}+\frac{1}{3^2}+\frac{1}{5^2}+\frac{1}{7^2}+\frac{1}{9^2}.....">
    </details>

19. **[Gregory-Leibniz Series - V](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Gregory-Leibiniz%20Series-V.py "Go tot Script")** :  Gregory-Leibniz Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi^3}{32}=\frac{1}{1^3}-\frac{1}{3^3}+\frac{1}{5^3}-\frac{1}{7^3}+\frac{1}{9^3}.....">
    </details>

20. **[Gregory-Leibniz Series - VI](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Gregory-Leibiniz%20Series-VI.py "Go tot Script")** :  Gregory-Leibniz Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{5\pi^5}{1536}=\frac{1}{1^5}-\frac{1}{3^5}+\frac{1}{5^5}-\frac{1}{7^5}+\frac{1}{9^5}.....">
    </details>

21. **[Gregory-Leibniz Series - VII](https://github.com/linjorejoy/Calulating-the-digits-of-pi/blob/master/Gregory-Leibiniz%20Series-VII.py "Go tot Script")** :  Gregory-Leibniz Series
    <details>
    <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\pi^6}{960}=\frac{1}{1^6}+\frac{1}{3^6}+\frac{1}{5^6}+\frac{1}{7^6}+\frac{1}{9^6}.....">
    </details>

<!-- 
Format for adding python scripts

1. **Heading** : <A small Definition>
   <details>
   <summary>Click to view Formula</summary>
      <img src="https://latex.codecogs.com/gif.latex?\dpi{5000}\alpha&space;+&space;\frac{2\beta}{\gamma}">
   </details>
 -->
<!-- <img src="https://latex.codecogs.com/svg.latex?\dpi{800}\Large&space;x=\frac{-b\pm\sqrt{b^2+4ac}}{2a}"/>


<img src="https://latex.codecogs.com/gif.latex?\dpi{5000}\alpha&space;+&space;\frac{2\beta}{\gamma}"> -->

<!-- 
SEARCH AND REPLACE
\*\*([A-Za-z \-'è]*)\*\*
**[$1]()** 
-->
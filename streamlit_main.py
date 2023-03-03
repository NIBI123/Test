import streamlit as st
st.set_page_config(layout="wide")

def intro():
    st.write("# Testng testing testing! 👋")
    st.write(
        """
        ### Premier Manager, Runde 10 (opdateret: 2023-03-03 07:00)
        Her er mit breakdown af de områder jeg vurderer er mest interessante:\n
        :red[Nketieh:] Her er jeg ikke i tvivl om at det er en spiller jeg sælger. Jeg ærgrer mig over at han står som skadet
         på holdet, da det formentlig vil få de fleste til at gå samme vej. Der er mange grunde til et salg imo.
         Nketieh har aldrig været en del af den ideele start 11'er. Han spiller Fordi Jesus er skadet. Jesus er iøvrigt i spil
         mid/slut marts, så vi nærmer os. Derfor SKAL nketieh ud snart alligevel. Og jeg tror han er tilbage i en reserve rolle.
         Baseret på hvordan Arteta har gjort generelt i år har jeg enormt svært ved at se ham gå væk fra Martinelli/Trossard/Saka,
         der har spillet fremragende på det sidste. Jeg ville blive MEGET overrasket må jeg indrømme. Nketieh er for dyr og optager en
         meget vigtig arsenal plads. Der er RIGELIGT med erstatninger. Ramsdale, White, Zinchenko, Saka, Ødegaard, Martinelli, Trossard, Saka 
         er alle glimrende køb\n
        :red[Man City:] Beholdt man City står man i en super fed situation da man får en ekstra mulighed her. City har dog blank runde om lidt så 
        køb ikke ind på City. Og sælg spillere der starter ude. Jeg ville blive chokeret hvis Lewis starter inde, så forvent et salg her.. \n
        :red[Brighton:] Vi afventer pressemødet idag ift. især March og tildels Estupinan. Personligt synes jeg dog Ferguson, Mitoma, March, MacAllister
        er klart de bedste Brighton køb. Beholdt man ikke march ville jeg klart gå med MacAllister. \n
        :red[Liverpool:] Liverpools defensiv har været on fire med 4 Clean sheets i træk, hvilket selvfølgelig hænger tæt sammen med Van Dijk der er tilbage. Det gør at jeg beholder Bajcetic. 
        Jeg tror stadig han er førstevalg. Nunez/Salah, hvis man gik ind på dem er straks sværere. Jeg havde et håb om at Leeds kunne drille Fulham i pokalen (38% sandsynlighed) 
        men de kan desværre ikke score på en chanec om det så galdt deres liv. Med blankrunde om 2 runder synes jeg derfor sagtens det kan forsvares at sælge dem igen, selvom det gør ondt.
        Nunez står til 64k i runden og 178k over de næste 2. Toney står f.eks. til 95k i runden og 222k over de næste 2. 
        Og så kan han beholdes længere. Jeg vil dog sige at jeg ikke synes det ville være forkert at beholde i to runder og
        så tage bestik af situationen der. Det KAN jo være at det dukker en spiller op om 2 runder.\n
        Salah Står til 209k over de næste 2, stort set lige med Toney, Kane og Ferguson. Derfor er han nemmere at beholde. \n
        :red[Øvrigt:] Kaptajnvalget er lidt et coin toss mellem Saka og Håland, så der må man gå med det man føler mest for. \n
        Mine transfers bliver formentlig Nketieh+Ogbonna+March+Nunez > Trossard+Mac Allister+Ferguson+Toney.
"""
    )
    st.write(
        """
        ### Super manager, Runde 3 (opdateret: 2023-03-03 07:00)
        Her er mit breakdown af de områder jeg vurderer er mest interessante:\n
        :red[Transferstrategi:] Vækstraterne har været enorme de første par runder, så betyder det at man skal ud i større udskiftninger? 
        Jeg hælder klart til nej, men værd at bemærke er det at vi ser væsentligt større favoritter hos bookmakerne nu end vi gjorde i efteråret.
        FCK 1.42, AGF 1.78, FCM 1.96, BIF 1.854, VFF 1.93. Det er væsentligt forskelligt fra efteråret hvor rundens største favorit ofte var 2.1 ish.
        Det giver naturligvis også udslag i modellen. Har man spillere fra ovenstående hold beholder man dem helt åbenlyst. Det samme gælder med
        FCN imo. Dermed vil manges hold være ret fyldte. Dilemmaet opstår ved Randers og Viborg der er rimelig populære pt. Det kedelige
        svar er at jeg synes man kan forsvare alle 3 beslutninger: Behold VFF, Behold RFC, behold begge. i SL manager kan man godt leve med 1 runde
        der formentlig vil være lidt svag, ift. hvis man beholder alle (jeg har selv 8 fra de to hold på mit bedste hold.). Ift. at sælge RFC ville jeg
        være meget tøvende da de har to glimrende kampe efter denne her (Hjemme mod AGF er en fin kamp..). Viborg er sværere, da de møder FCK+FCN i de næste to kampe.
        Den første hjemme mod FCN er dog en hvor man sagtens kunne beholde dem, medmindre man allerede har en 3-4 FCN spillere på holdet. 
        Jeg hælder selv mod at beholde VFF de næste 2 runder og sælge mine RFC spillere.\n
"""
    )
    
    df_playersValGWs = pd.read_csv('playersValGWs.csv')
    st.dataframe(df_playersValGWs)

page_names_to_funcs = {
    "Hovedside": intro,
}

demo_name = st.sidebar.selectbox("Vælg en side", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

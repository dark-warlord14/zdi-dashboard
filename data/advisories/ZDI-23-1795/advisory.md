# ZDI-23-1795: Schneider Electric EcoStruxure Power Monitoring Expert GetFilteredSinkProvider Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1795
- **ZDI-CAN:** ZDI-CAN-21035
- **Date:** 2023-12-15
- **CVE:** CVE-2023-5391
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Power Monitoring Expert
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1795/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStruxure Power Monitoring Expert. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GetFilteredSinkProvider method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-283-02&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-283-02.pdf

## Disclosure Timeline

- 2023-06-08 - Vulnerability reported to vendor
- 2023-12-15 - Coordinated public release of advisory

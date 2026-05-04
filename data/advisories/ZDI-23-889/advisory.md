# ZDI-23-889: Schneider Electric IGSS DashFiles Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-889
- **ZDI-CAN:** ZDI-CAN-20793
- **Date:** 2023-06-16
- **CVE:** CVE-2023-3001
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-889/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric IGSS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DashFiles class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-164-02&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-164-02.pdf

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory

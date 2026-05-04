# ZDI-22-346: (Pwn2Own) Western Digital MyCloud PR4100 samba Configuration Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-346
- **ZDI-CAN:** ZDI-CAN-15804
- **Date:** 2022-02-15
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Corentin BAYET (@OnlyTheDuck), Etienne HELLUY-LAFONT and Luca MORO (@johncool__) from Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-346/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the samba service. A crafted request can cause the service to overwrite a file. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://os5releasenotes.mycloud.com/#/

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory

# ZDI-22-1031: OPC Labs QuickOPC Connectivity Explorer Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1031
- **ZDI-CAN:** ZDI-CAN-16596
- **Date:** 2022-07-28
- **CVE:** CVE-2022-2561
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** OPC Labs
- **Affected Products:** QuickOPC
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of OPC Labs QuickOPC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XML files in Connectivity Explorer. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

OPC Labs has issued an update to correct this vulnerability. More details can be found at: https://kb.opclabs.com/ZDI-CAN-16596_Connectivity_Explorer_file_vulnerability

## Disclosure Timeline

- 2022-05-10 - Vulnerability reported to vendor
- 2022-07-28 - Coordinated public release of advisory

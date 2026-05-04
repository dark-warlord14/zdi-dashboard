# ZDI-21-339: (Pwn2Own) Synology DiskStation Manager StartEngCommPipeServer HandleSendMsg Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-339
- **ZDI-CAN:** ZDI-CAN-12361
- **Date:** 2021-03-22
- **CVE:** CVE-2021-27647
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** STARLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-339/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Synology DS418play. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the HandleSendMsg parameter sent to StartEngCommPipeServer. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/zh-hk/security/advisory/Synology_SA_20_26

## Disclosure Timeline

- 2021-03-17 - Vulnerability reported to vendor
- 2021-03-22 - Coordinated public release of advisory
- 2021-05-24 - Advisory Updated

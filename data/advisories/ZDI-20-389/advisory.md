# ZDI-20-389: Advantech WebAccess/NMS FwUpgradeAction Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-389
- **ZDI-CAN:** ZDI-CAN-9582
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10621
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-389/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the FwUpgradeAction.action endpoint. When parsing the filename element, the process does not properly validate user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-11-20 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory

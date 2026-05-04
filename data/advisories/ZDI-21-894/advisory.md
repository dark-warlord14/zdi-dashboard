# ZDI-21-894: (Pwn2Own) Microsoft Exchange Server OAB Arbitrary File Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-894
- **ZDI-CAN:** ZDI-CAN-13610
- **Date:** 2021-07-22
- **CVE:** CVE-2021-31198
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** rskvp93 of Team Viettel - Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-894/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the OAB service. The issue results from the lack of proper validation of user-supplied data, which can allow arbitrary files write to OAB folders. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2021-31198

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory

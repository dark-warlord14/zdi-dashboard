# ZDI-21-819: (Pwn2Own) Microsoft Exchange Server Arbitrary File Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-819
- **ZDI-CAN:** ZDI-CAN-13588
- **Date:** 2021-07-19
- **CVE:** CVE-2021-31207
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Orange Tsai(@orange_8361) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-819/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of mailbox export. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2021-31207

## Disclosure Timeline

- 2021-07-16 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory

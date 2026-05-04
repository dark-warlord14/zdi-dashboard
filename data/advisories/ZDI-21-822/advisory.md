# ZDI-21-822: (Pwn2Own) Microsoft Exchange Server PowerShell Improper Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-822
- **ZDI-CAN:** ZDI-CAN-13614
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34523
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** orangetw
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-822/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Powershell service. The issue results from the lack of proper validation of a access token prior to executing the Exchange PowerShell command. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory

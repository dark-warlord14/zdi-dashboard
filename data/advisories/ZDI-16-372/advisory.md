# ZDI-16-372: (Pwn2Own) Microsoft Windows Diagnostics Hub Standard Collector Directory Traversal Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-372
- **ZDI-CAN:** ZDI-CAN-3622
- **Date:** 2016-06-22
- **CVE:** CVE-2016-3231
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-372/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Diagnostics Hub Standard Collector. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within DiagnosticsHub.StandardCollector.Service.exe. The issue lies in the failure to properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-078

## Disclosure Timeline

- 2016-03-17 - Vulnerability reported to vendor
- 2016-06-22 - Coordinated public release of advisory

# ZDI-23-164: Microsoft Windows Untrusted Script Execution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-164
- **ZDI-CAN:** ZDI-CAN-18896
- **Date:** 2023-02-24
- **CVE:** CVE-2023-21805
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of certain image file types that can contain script tags. Under limited circumstances, crafted data in an image can lead to execution of untrusted script. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21805

## Disclosure Timeline

- 2022-11-03 - Vulnerability reported to vendor
- 2023-02-24 - Coordinated public release of advisory

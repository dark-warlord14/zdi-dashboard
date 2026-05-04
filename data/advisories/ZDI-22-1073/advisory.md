# ZDI-22-1073: Microsoft Windows Untrusted Script Execution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1073
- **ZDI-CAN:** ZDI-CAN-13069
- **Date:** 2022-08-18
- **CVE:** CVE-2022-30194
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1073/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of certain image file types, such as SVG, that can contain script tags. Under limited circumstances, crafted data in an image can lead to execution of untrusted script. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30194

## Disclosure Timeline

- 2022-02-23 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory

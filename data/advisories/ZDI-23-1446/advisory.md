# ZDI-23-1446: Microsoft Windows Untrusted Script Execution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1446
- **ZDI-CAN:** ZDI-CAN-20618
- **Date:** 2023-09-19
- **CVE:** CVE-2023-36805
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1446/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of certain image file types that can load scripts. Under limited circumstances, crafted data in an image can lead to execution of untrusted script. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36805

## Disclosure Timeline

- 2023-06-01 - Vulnerability reported to vendor
- 2023-09-19 - Coordinated public release of advisory

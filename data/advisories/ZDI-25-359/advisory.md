# ZDI-25-359: Microsoft Visual Studio initializeCommand Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-359
- **ZDI-CAN:** ZDI-CAN-26586
- **Date:** 2025-06-10
- **CVE:** CVE-2025-47959
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Nitesh Surana (@_niteshsurana) & Nelson William Gamazo Sanchez of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-359/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Visual Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the devcontainer.json file. When opening an project, the user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47959

## Disclosure Timeline

- 2025-02-19 - Vulnerability reported to vendor
- 2025-06-10 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated

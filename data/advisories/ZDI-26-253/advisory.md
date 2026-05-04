# ZDI-26-253: Microsoft Visual Studio Code mcp.json Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-253
- **ZDI-CAN:** ZDI-CAN-29184
- **Date:** 2026-04-02
- **CVE:** CVE-2026-21518
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio Code
- **Credit:** Amol Dosanjh, Dre Cura (@dre_cura), and Nicholas Zubrisky (@NZubrisky) of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Visual Studio Code. User interaction is required to exploit this vulnerability in that the target open a malicious project. The specific flaw exists within the handling of mcp.json files. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21518

## Disclosure Timeline

- 2026-03-05 - Vulnerability reported to vendor
- 2026-04-02 - Coordinated public release of advisory
- 2026-04-02 - Advisory Updated

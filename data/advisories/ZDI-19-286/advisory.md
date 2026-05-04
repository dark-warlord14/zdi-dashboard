# ZDI-19-286: Microsoft Windows ADODB Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-286
- **ZDI-CAN:** ZDI-CAN-7756
- **Date:** 2019-03-26
- **CVE:** CVE-2019-0784
- **CVSS:** 4.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-286/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. Interaction with a library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the module msado15.dll. Crafted data can trigger an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0784

## Disclosure Timeline

- 2018-12-31 - Vulnerability reported to vendor
- 2019-03-26 - Coordinated public release of advisory

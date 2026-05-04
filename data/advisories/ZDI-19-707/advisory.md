# ZDI-19-707: Microsoft Windows Font Subsetting Library Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-707
- **ZDI-CAN:** ZDI-CAN-7790
- **Date:** 2019-08-13
- **CVE:** CVE-2019-1144
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-707/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within fontsub.dll. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1144

## Disclosure Timeline

- 2019-01-25 - Vulnerability reported to vendor
- 2019-08-13 - Coordinated public release of advisory

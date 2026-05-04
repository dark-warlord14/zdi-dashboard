# ZDI-19-985: Microsoft Windows EMF Parsing Integer Truncation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-985
- **ZDI-CAN:** ZDI-CAN-9365
- **Date:** 2019-11-13
- **CVE:** CVE-2019-1441
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-985/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of EMF records. The issue results from the lack of proper validation of user-supplied data, which can result in an allocation of an undersized buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1441

## Disclosure Timeline

- 2019-09-05 - Vulnerability reported to vendor
- 2019-11-13 - Coordinated public release of advisory

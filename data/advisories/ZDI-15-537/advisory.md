# ZDI-15-537: Microsoft Windows VBScript Join Function Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-537
- **ZDI-CAN:** ZDI-CAN-3327
- **Date:** 2015-11-10
- **CVE:** CVE-2015-6055
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun - HPE Security Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-537/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code in applications using the VBScript scripting language running on vulnerable installations of Microsoft Windows. Microsoft Internet Explorer is an affected application. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Join function in VBScript. By passing unexpected arguments to this function, an attacker can cause an integer to be incorrectly interpreted as a pointer to an object in memory. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-108

## Disclosure Timeline

- 2015-09-22 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory

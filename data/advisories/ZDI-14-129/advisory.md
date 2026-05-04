# ZDI-14-129: Microsoft DIA SDK msdia.dll Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-129
- **ZDI-CAN:** ZDI-CAN-1856
- **Date:** 2014-05-14
- **CVE:** CVE-2014-3802
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Debug Interface Access SDK
- **Credit:** 80ceb6400c43bd3fa9f1ef561f7c51d929fe0199
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Debug Interface Access SDK. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDB files. The issue lies in a failure to sanitize a value which is then used in the calculation of an address for a dynamic call. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://go.microsoft.com/fwlink/p/?LinkId=306566

## Disclosure Timeline

- 2013-05-13 - Vulnerability reported to vendor
- 2014-05-14 - Coordinated public release of advisory

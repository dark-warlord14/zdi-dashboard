# ZDI-15-538: Microsoft Internet Explorer COptionElement::InvalidateDataListAncestorCollections Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-538
- **ZDI-CAN:** ZDI-CAN-2915
- **Date:** 2015-11-10
- **CVE:** CVE-2015-6064
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun - HPE Security Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-538/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer caches the options collection of datalist elements. By manipulating a document's elements an attacker can force a COptionElement object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-112

## Disclosure Timeline

- 2015-05-06 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory

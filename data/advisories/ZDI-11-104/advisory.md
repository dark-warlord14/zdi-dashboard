# ZDI-11-104: (Pwn2Own) Webkit CSS Text Element Count Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-104
- **ZDI-CAN:** ZDI-CAN-1107
- **Date:** 2011-04-14
- **CVE:** CVE-2011-1290
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** WebKit
- **Affected Products:** WebKit
- **Credit:** Anonymous Vincenzo Iozzo, Willem Pinckaers, and Ralf-Philipp Weinmann
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-104/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WebKit library's implementation of a CSS style. When totaling the length of it's string elements, the library will store the result into a 32bit integer. This value will be used for an allocation and then later will be used to initialize the allocated buffer. Due to the number of elements being totaled being variable, this will allow an aggressor to provide as many elements as necessary in order to cause the integer value to wrap causing an under-allocation. Initialization of this data will then cause a heap-based buffer overflow. This can lead to code execution under the context of the application.

## Additional Details

Apple patch on April 14, 2011: http://support.apple.com/kb/HT4606 http://support.apple.com/kb/HT4607 http://support.apple.com/kb/HT4596 Webkit fix: http://trac.webkit.org/changeset/80787 http://trac.webkit.org/changeset/82054

## Disclosure Timeline

- 2011-03-31 - Vulnerability reported to vendor
- 2011-04-14 - Coordinated public release of advisory

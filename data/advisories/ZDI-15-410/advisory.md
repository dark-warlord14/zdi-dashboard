# ZDI-15-410: (0Day) Corel WordPerfect Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-410
- **ZDI-CAN:** ZDI-CAN-3052
- **Date:** 2015-09-02
- **CVE:** CVE-2015-6948
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Corel
- **Affected Products:** WordPerfect
- **Credit:** Dave Weinstein - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-410/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Corel WordPerfect. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion from documents formatted for Microsoft Word. By providing a malformed file, an attacker can cause memory to be written past the end of a heap buffer. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 07/28/2015 - ZDI Coordinator sat in a vendor chat help window waiting for assistance without response 07/28/2015 - ZDI emailed vendor and requested contact 08/13/2015 - ZDI emailed vendor and requested contact 08/21/2015 - ZDI emailed vendor and requested contact -- Mitigation: Given the stated purpose of Corel WordPerfect, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2015-05-05 - Vulnerability reported to vendor
- 2015-09-02 - Coordinated public release of advisory

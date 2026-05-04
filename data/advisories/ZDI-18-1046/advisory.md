# ZDI-18-1046: (0Day) PoDoFo Library ParseToUnicode Memory Corruption Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1046
- **ZDI-CAN:** ZDI-CAN-5673
- **Date:** 2018-09-13
- **CVE:** CVE-2018-14320
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** PoDoFo
- **Affected Products:** PoDoFo
- **Credit:** V.E.O of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1046/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of PoDoFo Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within PdfEncoding::ParseToUnicode(). The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/10/18 - ZDI reported the vulnerability to the vendor 04/10/18 - The vendor acknowledged 08/17/18 - ZDI contacted the vendor requesting a status update 08/18/18 - The vendor indicated fixes were not available yet 08/20/18 - ZDI requested an ETA for the fix and notified the vendor the intention to 0-day -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-04-10 - Vulnerability reported to vendor
- 2018-09-13 - Coordinated public release of advisory
- 2018-09-13 - Advisory Updated

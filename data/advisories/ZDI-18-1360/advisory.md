# ZDI-18-1360: (0Day) INVT Electric VT-Designer File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1360
- **ZDI-CAN:** ZDI-CAN-6414
- **Date:** 2018-11-26
- **CVE:** CVE-2018-18983
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** INVT
- **Affected Products:** VT-Designer
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1360/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of INVT VT-Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of pm3 files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-07-25 - Vulnerability reported to vendor
- 2018-11-26 - Coordinated public release of advisory
- 2018-11-29 - Advisory Updated

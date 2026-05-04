# ZDI-18-1361: (0Day) INVT Electric VT-Designer PM3 File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1361
- **ZDI-CAN:** ZDI-CAN-6428
- **Date:** 2018-11-26
- **CVE:** CVE-2018-18987
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** INVT
- **Affected Products:** VT-Designer
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1361/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of INVT VT-Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CArchive objects. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/26/18 - ZDI reported the vulnerability to ICS-CERT 11/21/18 - ZDI contacted ICS-CERT requesting a status update 11/21/18 - ICS-CERT indicated that the issue was pending disclosure until the vendor confirmed the right recipient 11/21/18 - ZDI notified ICS-CERT the case will 0-day on November 26 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-07-26 - Vulnerability reported to vendor
- 2018-11-26 - Coordinated public release of advisory
- 2018-11-29 - Advisory Updated

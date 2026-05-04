# ZDI-18-1088: (0Day) Fuji Electric Alpha5 Smart Loader C5V File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1088
- **ZDI-CAN:** ZDI-CAN-6241
- **Date:** 2018-09-26
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha Loader
- **Credit:** Michael Flanders of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fuji Electric Alpha Loader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of C5V files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/19/18 - ZDI reported the vulnerability to ICS-CERT 09/19/18 - ZDI asked ICS-CERT for a status update 09/19/18 - ICS-CERT notified ZDI that the vendor has budgeted for and is working on a fix, but does not yet have any ETA 09/21/18 - ZDI notified ICS-CERT of the intent to disclose the report as an 0-day advisory on 9/26 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-22 - Vulnerability reported to vendor
- 2018-09-26 - Coordinated public release of advisory
- 2018-09-26 - Advisory Updated

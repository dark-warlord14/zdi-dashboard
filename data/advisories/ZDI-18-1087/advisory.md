# ZDI-18-1087: (0Day) Fuji Electric Alpha5 Smart Loader A5P File Parsing Buffer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1087
- **ZDI-CAN:** ZDI-CAN-6240
- **Date:** 2018-09-26
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha Loader
- **Credit:** Michael Flanders of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1087/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Fuji Electric Alpha Loader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of A5P files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/24/18 - ZDI reported the vulnerability to ICS-CERT 09/17/18 - ZDI asked ICS-CERT for a status update 09/26/18 - ZDI notified ICS-CERT of the intent to disclose the report as an 0-day advisory on 9/26 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-24 - Vulnerability reported to vendor
- 2018-09-26 - Coordinated public release of advisory
- 2018-09-26 - Advisory Updated

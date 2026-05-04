# ZDI-18-1085: (0Day) Fuji Electric Frenic Loader FNC File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1085
- **ZDI-CAN:** ZDI-CAN-6238
- **Date:** 2018-09-26
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Frenic Loader
- **Credit:** Michael Flanders of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1085/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Fuji Electric Frenic Loader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of FNC files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to disclose sensitive information under the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/22/18 - ZDI reported the vulnerability to ICS-CERT 07/10/18 - ICS-CERT replied that the vendor requested a deadline extension due to work between remote teams 07/10/18 - The vendor requested feedback on one of their proposed solutions for the issues 07/12/18 - ZDI offered a one week extension to the deadline 07/16/18 - ZDI provided feedback on the proposed fix as requested 08/02/18 - ZDI requested an update and any ETA 08/10/18 - ICS-CERT sent a reply from the vendor that a fix "will require significant effort because the change requires modification to the core components of our software package" 08/14/18 - ZDI replied “several months" extension is not something we can provide 09/19/18 - ZDI notified ICS-CERT of the intent to disclose these reports as 0-day advisories on 9/26 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-22 - Vulnerability reported to vendor
- 2018-09-26 - Coordinated public release of advisory
- 2018-09-26 - Advisory Updated

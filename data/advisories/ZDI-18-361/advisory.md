# ZDI-18-361: (0Day) Advantech WebAccess HMI Designer PM3 File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-361
- **ZDI-CAN:** ZDI-CAN-5246
- **Date:** 2018-04-20
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess HMI Designer
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-361/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess HMI Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of a PM3 file. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/17/17 - ZDI reported vulnerabilities to ICS-CERT 10/23/17 - ICS-CERT provided ZDI with one ICS-VU # for each case 03/13/18 - ZDI contacted ICS-CERT requesting a status update 03/26/18 - ZDI contacted ICS-CERT again requesting a status update 03/28/18 - ZDI contacted ICS-CERT again requesting a status update 03/28/18 - ICS-CERT replied they were waiting for status update from vendor 04/13/18 - ZDI notified ICS-CERT these cases will 0-day on April 20th -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2017-10-17 - Vulnerability reported to vendor
- 2018-04-20 - Coordinated public release of advisory
- 2018-04-20 - Advisory Updated

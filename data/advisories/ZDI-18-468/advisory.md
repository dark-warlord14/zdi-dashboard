# ZDI-18-468: (0Day) Delta Industrial Automation TPEditor TPE File Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-468
- **ZDI-CAN:** ZDI-CAN-5389
- **Date:** 2018-05-16
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** TPEditor
- **Credit:** Robert Hawes / Twitter @VulnMind
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-468/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation TPEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of TPE files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/13/17 - ZDI reported vulnerability to ICS-CERT 12/19/17 - ICS-CERT provided ZDI with ICS-VU # 12/20/17 - ICS-CERT confirmed vendor had reproduced the issue 03/29/18 - ICS-CERT mentioned vendor asked for an extension of 1 month (original deadline April 11th) 04/02/18 - ZDI asked for vendor's ETA and agreed on an extra week, but not a month 05/14/18 - ZDI requested status update indicating the case will 0-day on Wednesday May 16th 05/14/18 - ICS-CERT confirmed vendor had been notified of the 0-day plan and had also been requested status update -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2017-12-13 - Vulnerability reported to vendor
- 2018-05-16 - Coordinated public release of advisory
- 2018-06-20 - Advisory Updated

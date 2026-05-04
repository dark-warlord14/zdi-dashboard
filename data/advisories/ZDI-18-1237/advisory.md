# ZDI-18-1237: Delta Industrial Automation TPEditor TPE File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1237
- **ZDI-CAN:** ZDI-CAN-6449
- **Date:** 2018-10-15
- **CVE:** CVE-2018-17927
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** TPEditor
- **Credit:** Ariele Caltabiano (kimiya) of 9SG Security Team - kimiya@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1237/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation TPEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TPE files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-284-03

## Disclosure Timeline

- 2018-06-28 - Vulnerability reported to vendor
- 2018-10-15 - Coordinated public release of advisory
- 2018-10-15 - Advisory Updated

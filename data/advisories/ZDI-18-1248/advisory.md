# ZDI-18-1248: LAquis SCADA LQS File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1248
- **ZDI-CAN:** ZDI-CAN-6279
- **Date:** 2018-10-16
- **CVE:** CVE-2018-17897
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** rgod of 9SG Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1248/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LAquis SCADA Software. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of LQS files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. At attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-289-01

## Disclosure Timeline

- 2018-05-24 - Vulnerability reported to vendor
- 2018-10-16 - Coordinated public release of advisory
- 2018-10-16 - Advisory Updated

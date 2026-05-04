# ZDI-19-060: LAquis SCADA LQS File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-060
- **ZDI-CAN:** ZDI-CAN-6670
- **Date:** 2019-01-19
- **CVE:** CVE-2018-18994
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-060/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LQS files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated

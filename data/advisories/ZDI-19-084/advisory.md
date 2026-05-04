# ZDI-19-084: LAquis SCADA LGX Report Memory Byte Untrusted Pointer Dereference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-084
- **ZDI-CAN:** ZDI-CAN-6621
- **Date:** 2019-01-19
- **CVE:** CVE-2018-18988
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-084/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of LAquis SCADA Software. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the Memory.Byte method. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the aq process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-09-11 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated

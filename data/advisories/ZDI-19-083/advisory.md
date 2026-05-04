# ZDI-19-083: LAquis SCADA LGX Report MemoryWriteWord Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-083
- **ZDI-CAN:** ZDI-CAN-6620
- **Date:** 2019-01-19
- **CVE:** CVE-2018-18988
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LAquis SCADA Software. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the MemoryWriteWord method. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the aq process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-09-11 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated

# ZDI-19-096: LAquis SCADA LGX Report File BlockWrite Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-096
- **ZDI-CAN:** ZDI-CAN-6681
- **Date:** 2019-01-19
- **CVE:** CVE-2018-18988
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LAquis SCADA Software. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of LGX report files. Script embedded in a crafted file can create files in arbitrary locations using the File.BlockWrite method. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-09-11 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated

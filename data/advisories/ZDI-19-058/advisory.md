# ZDI-19-058: LAquis SCADA Web Server Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-058
- **ZDI-CAN:** ZDI-CAN-6667
- **Date:** 2019-01-19
- **CVE:** CVE-2018-18990
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-058/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of LAquis SCADA Software. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requested URLs. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the aq process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated

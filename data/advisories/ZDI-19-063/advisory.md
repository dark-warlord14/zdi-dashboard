# ZDI-19-063: LAquis SCADA Web Server acompanhamentotela TAGALTERE Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-063
- **ZDI-CAN:** ZDI-CAN-6673
- **Date:** 2019-01-19
- **CVE:** CVE-2018-18992
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-063/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LAquis SCADA Software. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to acompanhamentotela.lhtml. When parsing the TAGALTERE Element, the process does not properly sanitize user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code under the context of the aq process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated

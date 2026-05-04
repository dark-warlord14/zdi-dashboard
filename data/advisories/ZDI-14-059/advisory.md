# ZDI-14-059: Schneider-Electric ClearSCADA ServerMain.exe OPF File Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-059
- **ZDI-CAN:** ZDI-CAN-1876
- **Date:** 2014-04-03
- **CVE:** CVE-2014-0779
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** ClearSCADA
- **Credit:** Andrew Brooks
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-059/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider-Electric ClearSCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of OPF files. The issue lies in a failure to validate a length specifier before using it as an index into an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-072-01

## Disclosure Timeline

- 2014-01-13 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory

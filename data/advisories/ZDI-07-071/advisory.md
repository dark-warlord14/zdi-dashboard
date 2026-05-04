# ZDI-07-071: Hewlett-Packard OpenView Network Node Manager Multiple CGI Buffer Overflow Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-07-071
- **ZDI-CAN:** ZDI-CAN-111
- **Date:** 2007-12-06
- **CVE:** CVE-2007-6204
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-071/
## Vulnerability Details

These vulnerabilities allow remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard (HP) OpenView Network Node Manager (NNM). Authentication is not required to exploit these vulnerabilities. The specific flaws exists within the CGI applications that handle the management of the NNM server. Due to lack of bounds checking during a call to sprintf(), sending overly long arguments to the various CGI variables result in a classic stack overflow leading to compromise of the remote server. Exploitation leads to code execution running under the credentials of the web server. Further techniques can be leveraged to gain full SYSTEM access. The following is a list of vulnerable CGI applications: - ovlogin.exe - OpenView5.exe - snmpviewer.exe - webappmon.exe

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found in HP Security Bulletin Document ID c01188923.

## Disclosure Timeline

- 2006-10-10 - Vulnerability reported to vendor
- 2007-12-06 - Coordinated public release of advisory

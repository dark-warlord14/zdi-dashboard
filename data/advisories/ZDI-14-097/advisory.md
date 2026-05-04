# ZDI-14-097: CA ERwin Web Portal MIMM ProfileIconServlet Multiple Information Disclosure Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-14-097
- **ZDI-CAN:** ZDI-CAN-2018
- **Date:** 2014-04-17
- **CVE:** CVE-2014-2210
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** CA
- **Affected Products:** ERwin Web Portal
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-097/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary files on a system with vulnerable installations of CA ERwin Web Portal's Meta Integration Metadata Management service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the "Meta Integration Web Server and Services" ProfileIconServlet which is vulnerable to directory traversals in multiple parameters. An attacker can leverage these vulnerabilities to read arbitrary files, including files which store database credentials, under the context of SYSTEM. An attacker can couple this vulnerability with others to gain remote code execution.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={7F968A14-7407-4BCF-9EB1-EFE9F0E6D663}

## Disclosure Timeline

- 2014-04-11 - Vulnerability reported to vendor
- 2014-04-17 - Coordinated public release of advisory

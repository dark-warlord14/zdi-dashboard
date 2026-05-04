# ZDI-14-096: CA ERwin Web Portal MIMM FileAccessServiceProvider Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-096
- **ZDI-CAN:** ZDI-CAN-2017
- **Date:** 2014-04-17
- **CVE:** CVE-2014-2210
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** CA
- **Affected Products:** ERwin Web Portal
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-096/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on a system with vulnerable installations of CA ERwin Web Portal's Meta Integration Metadata Management service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the "Meta Integration Web Server and Services" fileaccess provider which is vulnerable to a directory traversal. An attacker can leverage this vulnerability to delete arbitrary files recursively, including operating system files, as the service is installed with SYSTEM privileges by default.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={7F968A14-7407-4BCF-9EB1-EFE9F0E6D663}

## Disclosure Timeline

- 2014-04-11 - Vulnerability reported to vendor
- 2014-04-17 - Coordinated public release of advisory

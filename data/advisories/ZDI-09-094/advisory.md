# ZDI-09-094: Hewlett-Packard OpenView NNM Multiple Command Injection Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-09-094
- **ZDI-CAN:** ZDI-CAN-453
- **Date:** 2009-12-09
- **CVE:** CVE-2009-3845
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Network Node Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard's Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaws exist within Perl CGI executables distributed with Network Node Manager (NNM). Several of these applications fail to sanitize the hostname HTTP variable when requests are made to the NNM HTTP server which listens by default on TCP port 3443. By supplying a pipe operator a malicious attacker can insert arbitrary commands that will be executed on the remote server.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01950877

## Disclosure Timeline

- 2009-03-13 - Vulnerability reported to vendor
- 2009-12-09 - Coordinated public release of advisory

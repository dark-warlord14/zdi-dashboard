# ZDI-06-039: Marshal MailMarshal ARJ Extraction Directory Traversal Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-039
- **ZDI-CAN:** ZDI-CAN-003
- **Date:** 2006-11-10
- **CVE:** CVE-2006-5487
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** NetIQ
- **Affected Products:** MailMarshal
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Marshal MailMarshal (formerly of NetIQ). Authentication is not required to exploit this vulnerability. The specific flaw exists within the extraction and scanning of ARJ compressed attachments. Due to incorrect sandboxing of extracted filenames that contain directory traversal modifiers such as "../", an attacker can cause an executable to be created in an arbitrary location. While currently existing files can not be over written, an attacker may leverage this vulnerability in a number of ways. For example, by placing a malicious binary in the "all users" startup folder.

## Additional Details

NetIQ has issued an update to correct this vulnerability. More details can be found at: http://www.marshal.com/kb/article.aspx?id=11450

## Disclosure Timeline

- 2006-07-17 - Vulnerability reported to vendor
- 2006-11-10 - Coordinated public release of advisory

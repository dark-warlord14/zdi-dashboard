# ZDI-11-153: Embarcadero Interbase connect Request Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-153
- **ZDI-CAN:** ZDI-CAN-244
- **Date:** 2011-04-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Embarcadero
- **Affected Products:** Interbase
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-153/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Borland Interbase. Authentication is not required to exploit these vulnerabilities. The specific flaws exists within the database service, ibserver.exe, which binds to TCP port 3050. When a specially crafted "connect" (opcode 0x01) message is sent a stack-based buffer overflow can occur. If properly exploited this can lead to remote compromise of the system with SYSTEM credentials.

## Additional Details

This issue is now resolved in InterBase XE update 2. This update is available from http://cc.embarcadero.com/reg/interbase . On that page, there are multiple downloads which contain this fix. Below are the descriptions of all the downloads that have this fix. Note that each description has two downloads, one for English and one for Japanese. InterBase XE 64-bit Update 2 (10.0.2.474) for Windows InterBase XE Update 2 (10.0.2.467) for Linux InterBase XE 32-bit Update 2 (10.0.2.474) for Windows The readme document in the download has a list of defects resolved.

## Disclosure Timeline

- 2011-02-04 - Vulnerability reported to vendor
- 2011-04-29 - Coordinated public release of advisory
